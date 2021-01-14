#define POT_OPCODE_WRITE    0b0001
#define POT_OPCODE_OFF      0b0010
#define POT_SELECT_0        0b0001
#define POT_SELECT_1        0b0010
#define POT_SELECT_BOTH     0b0011

void writePot(unsigned char value);
void setPot(unsigned char value);
unsigned char getMax (unsigned char xx, unsigned char yy);
unsigned char getMin(unsigned char xx, unsigned char yy);
