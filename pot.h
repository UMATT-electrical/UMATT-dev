#ifndef POT_H_
#define POT_H

#define POT_OPCODE_WRITE    0b0001
#define POT_OPCODE_OFF      0b0010
#define POT_SELECT_0        0b0001
#define POT_SELECT_1        0b0010
#define POT_SELECT_BOTH     0b0011

void writePot(uint8_t value);
void setPot(uint8_t value);
uint8_t getMax (uint8_t value1, uint8_t value2);
uint8_t getMin(uint8_t value1, uint8_t value2);

#endif
