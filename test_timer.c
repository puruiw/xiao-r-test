#include <stdio.h>
#include <time.h>

const long BILLION = 1000 * 1000 * 1000;
const long SLEEP_NS = 1000;
const long LOOP = BILLION / SLEEP_NS;
const clockid_t CLOCK = CLOCK_MONOTONIC;

// Overhead is very high.
void nsleep(long ns) {
    struct timespec req = {0, ns}, rem;
    nanosleep(&req, &rem);
}

void timespec_add(struct timespec* output, const struct timespec* input, long ns) {
    output->tv_sec = input->tv_sec;
    output->tv_nsec = input->tv_nsec + ns;
    if (output->tv_nsec > BILLION) {
        output->tv_nsec -= BILLION;
        output->tv_sec += 1;
    }
}

int timespec_less(const struct timespec* a, const struct timespec* b) {
    return (a->tv_sec < b->tv_sec) || (
            (a->tv_sec == b->tv_sec) && (a->tv_nsec < b->tv_nsec));
}

// On Raspberry Pi 3. This function has a 2.5e-7s overhead per call.
void busy_loop(long ns) {
    struct timespec start, end, current;
    clock_gettime(CLOCK, &start);
    timespec_add(&end, &start, ns);
    while (1) {
        clock_gettime(CLOCK, &current);
        if (timespec_less(&end, &current))
            break;
    }
}

void test_sleep(void (*sleep_f)(long)) {
    struct timespec start, end;
    clock_gettime(CLOCK, &start);

    for (int i = 0; i < LOOP; i++) {
        sleep_f(SLEEP_NS);
    }

    clock_gettime(CLOCK, &end);
    printf("%.5f\n", (end.tv_sec - start.tv_sec) + 1.0e-9 * (end.tv_nsec - start.tv_nsec));
    return;
}

int main(int argc, char* argv[]) {
    // test_sleep(nsleep);
    test_sleep(busy_loop);
    return 0;
}
