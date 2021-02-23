#ifndef SPI_H_
#define SPI_H_

struct Message;
struct Message msgMkr(unsigned long data, unsigned char size);
void writeSPI(uint8_t CS, struct Message data);
uint8_t getBit(uint8_t idx, uint32_t data);
uint16_t readSPI(uint8_t CS, uint8_t length);

#endif
