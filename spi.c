/**
 * SPI_C
 * @author K Gledson
 * @version 2021-01-21
 * Functions needed for Serial Peripheral Interface (SPI) communication
 */

///////////////////////////////////////////////////////////////////////////////////////// included files (get rid of these later)
#include "stdint.h" //library not found on my computer.
#include "spi.h"
#include "definitions.h"
///////////////////////////////////////////////////////////////////////////////////////// functions

struct Message {
   uint32_t operation; 	//message to be sent over SPI
   uint8_t 	length;		//message length
};//Message

struct Message msgMkr(uint32_t data, uint8_t size){
    struct Message msg;
    msg.operation = data;
    msg.length = size;
    return msg;
}//msgMkr

void writeSPI(uint8_t CS, struct Message data){
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
        data = data<<1 + digitalRead(MISO);
        digitalWrite(CLK,LOW);
        //add sleep function for 0.005 seconds
    }
    digitalWrite(CS, HIGH);
    return data;
}//readSPI
