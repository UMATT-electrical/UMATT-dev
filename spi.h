struct Message;
struct Message msgMkr(unsigned long data, unsigned char size);
void writeSPI(unsigned char CS, struct Message data);
unsigned char getBit(unsigned char idx, unsigned char data);
unsigned char readSPI(unsigned char CS);
