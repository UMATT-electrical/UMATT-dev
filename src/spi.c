/**
 * SPI_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed for Serial Peripheral Interface (SPI) communication
 */
#include "spi.h"

message_32b msgMkr(uint32_t data, uint8_t size){
    message_32b msg;
    msg.operation = data;
    msg.length = size;
    return msg;
}//msgMkr

void writeSPI(uint8_t CS, struct Message_32b data){
    digitalWrite(CS, LOW);
    for (int i=0; i<data.length; i++){
        digitalWrite(MOSI,getBit(i,data.operation));
        digitalWrite(CLK,HIGH);
        //add sleep function for 0.005 seconds
        digitalWrite(CLK,LOW);
        //add sleep function for 0.005 seconds
    }
    digitalWrite(MOSI, LOW);
    digitalWrite(CS, HIGH);
    //add sleep function for 0.005 seconds
}//writeSPI

uint8_t getBit(uint8_t idx, uint32_t data){
    return (data & (1 << idx)) >> idx;
}//getBit

uint16_t readSPI(uint8_t CS, uint8_t length){
    uint16_t data;
    digitalWrite(CS, LOW);
    for (int i=0; i<length; i++){
         digitalWrite(CLK,HIGH);
         //add sleep function for 0.005 seconds
        for(int t=0; t<1000000; t++){}
        data = data<<1 + digitalRead(MISO);
        digitalWrite(CLK,LOW);
        for(int t=0; t<1000000; t++){}
        //add sleep function for 0.005 seconds
    }
    digitalWrite(CS, HIGH);
    return data;
}//readSPI
