struct Message {
   unsigned long word
   unsigned char length 
}//Message

struct Message msgMkr(unsigned long data, unsigned char size){
    struct Message msg;
    msg.word = data;
    msg.length = size;
    return msg
}//msgMkr

void initGPIO(unsigned char CS){
    /*Assigns register A as all input and register B as all output
      Verify this is acceptable for all GPIOs on the board*/
    unsigned long input = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRA<<8)+ALL_INPUT;
    unsigned long output = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRB<<8)+ALL_OUTPUT;
    struct Message messageA = msgMkr(input,24);
    struct Message messageB = msgMkr(output,24);
    writeSPI(CS,messageA);                                                              //Write Port A configuration over SPI
    writeSPI(CS,messageB);                                                              //Write Port B configuration over SPI
}//initGPIO

void writeGPIO(unsigned char CS, unsigned char register, unsigned char byte){
    unsigned long word = (GPIO_OPCODE_WRITE<<16)+(register<<8)+byte; 
    struct Message message = msgMkr(word,24);
    writeSPI(CS,message);
}//writeGPIO

unsigned char readGPIO(unsigned char CS, unsigned char register){
    unsigned char data;
    unsigned long word = (GPIO_OPCODE_READ<<8)+register;
    struct Message message = msgMkr(word, 16);
    writeSPI(CS, message);
    return readSPI(CS);
}//readGPIO

