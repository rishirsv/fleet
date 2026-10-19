#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

#if defined(__GNUC__) || defined(__clang__)
#define NOINLINE __attribute__((noinline))
#else
#define NOINLINE
#endif

NOINLINE uint32_t checksum(const uint8_t *buf, size_t n) {
    uint32_t value = UINT32_C(2166136261);
    for (size_t i = 0; i < n; ++i) {
        value ^= buf[i];
        value *= UINT32_C(16777619);
    }
    return value;
}

NOINLINE int valid_record(const uint8_t *buf, size_t n) {
    if (n < 4) return 0;
    if (buf[0] != 'R' || buf[1] != 'E') return 0;
    if (buf[2] != 1) return 0;
    return buf[3] <= 32;
}

int main(void) {
    const uint8_t record[] = {'R', 'E', 1, 8, 0xAA};
    printf("valid=%d checksum=%08x\n",
           valid_record(record, sizeof record),
           (unsigned int)checksum(record, sizeof record));
    return 0;
}
