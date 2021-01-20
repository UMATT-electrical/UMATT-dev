/**
 * GPIO_C
 * @author K Gledson
 * @version 2021-01-20
 *
 */

void initGPIO(unsigned char CS){
    /*Assigns register A as all input and register B as all output
      Verify this is acceptable for all GPIOs on the board*/
    unsigned long input = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRA<<8)+ALL_INPUT;		//opcode to make all pins inputs
    unsigned long output = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRB<<8)+ALL_OUTPUT;	//opcode to make all pins outputs
    struct Message messageA = msgMkr(input,24);											//assign all input message for SPI
    struct Message messageB = msgMkr(output,24);										//assign all output message for SPI
    writeSPI(CS,messageA);                                                              //Write Port A configuration over SPI
    writeSPI(CS,messageB);                                                              //Write Port B configuration over SPI
}//initGPIO

void writeGPIO(unsigned char CS, unsigned char bank, unsigned char byte){
    unsigned long word = (GPIO_OPCODE_WRITE<<16)+(bank<<8)+byte;
    struct Message message = msgMkr(word,24);
    writeSPI(CS,message);
}//writeGPIO


unsigned char readGPIO(unsigned char CS, unsigned char bank){
    unsigned char data;
    unsigned long word = (GPIO_OPCODE_READ<<8)+bank;
    struct Message message = msgMkr(word, 16);
    writeSPI(CS, message);
    return readSPI(CS);
}//readGPIO


