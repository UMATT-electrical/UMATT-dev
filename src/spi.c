/**
 * SPI_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed for Serial Peripheral Interface (SPI) communication
 */
#include "spi.h"

//MCP23s17 specific timings:
//20ns between signal lo/hi on chip read @1.8V-5.5V (spec: table 1-4[4,5])
const struct timespec *writeSleepTimer = (const struct timespec[]){{0,100l}};
//90ns between signal hi/lo on chip write @1.8V-5.5V (spec: table 1-4[8,9])
const struct timespec *readSleepTimer = (const struct timespec[]){{0,100l}};


/**FIXME: Add description
 * 
 * 
 */ 
message_32b msgMkr(uint32_t data, uint8_t size){
    message_32b msg;
    msg.operation = data;
    msg.length = size;
    return msg;
}//msgMkr

/**FIXME: Add description
 * 
 * 
 */ 
uint8_t getBit(uint8_t idx, uint32_t data){
    return (data & (1 << idx)) >> idx;
}//getBit

/** SPI Write for a MCP23s17
 * @param CS:
 * @param data:
 * 
 * See 3.2.3 for spec details on the "MCP23s17-E SP.pdf"
 */ 
void writeSPI(uint8_t CS, struct Message_32b data){
    digitalWrite(CS, LOW);
    for(int t=0; t<1000000; t++){}
    //MCP23s17 needs MSB->LSB (spec: figure 1-5)
    //This is why we loop from the top and work down
    for (int i=data.length-1; -1<i; i--){
        //MCP23s17 reads on a rising edge (spec: figure 1-5)
        digitalWrite(MOSI,getBit(i,data.operation));
        nanosleep(writeSleepTimer, NULL);
        digitalWrite(CLK,HIGH);
        nanosleep(writeSleepTimer, NULL);
        digitalWrite(CLK,LOW);
    }
    digitalWrite(MOSI, LOW);
    digitalWrite(CS, HIGH);
}//writeSPI

/**FIXME: Add description
 * @param CS:
 * @param length:
 * 
 * @return data: 
 * 
 * See spec details on the "MCP23s17-E SP.pdf"
 */ 
uint16_t readSPI(uint8_t CS, uint8_t length){
    uint16_t data;
    digitalWrite(CS, LOW);
    for (int i=0; i<length; i++){
        //MCP23s17 writes on rising edge (spec: figure 1-6)
        digitalWrite(CLK,HIGH);
        nanosleep(readSleepTimer, NULL);
        //FIXME: Should we be stuffing this in a Message_32b for consistency?
        data = (data<<1) + digitalRead(MISO);
        digitalWrite(CLK,LOW);
        nanosleep(readSleepTimer, NULL);
    }
    digitalWrite(CS, HIGH);
    return data;
}//readSPI
