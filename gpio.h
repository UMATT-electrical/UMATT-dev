#ifndef GPIO_H_
#define GPIO_H_

#define GPIO_OPCODE_WRITE       0b01000000
#define GPIO_OPCODE_READ        0b01000001
#define GPIO_SELECT_DIRA		0x00
#define GPIO_SELECT_DIRB		0x01
#define GPIO_SELECT_PORTA		0x12
#define GPIO_SELECT_PORTB		0x13
#define GPIO_SELECT_GPPUA       0x0C
#define GPIO_INIT_DELAY			10
#define ALL_OUTPUT				0b00000000
#define ALL_INPUT				0b11111111
#define GPPUA_ENABLE_ALL        0b11111111
#define BANK_SIZE				8

void initGPIO(void);
void initGPIO1(void);
void initGPIO2(void);
void initGPIO3(void);
void initGPIO4(void);
void writeGPIO(uint8_t CS, uint16_t bank, uint8_t byte);
uint16_t readGPIO(uint8_t CS, uint16_t bank);

#endif
