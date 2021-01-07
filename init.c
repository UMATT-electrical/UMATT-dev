#include "GPIODefinitions.h"
#include "definitions.h"
#include <wiringPi.h>
#include <stdio.h>

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

void initPin(){
    //Sets direction of header pins
    pinmode(MOSI,OUTPUT);       //Data ouput pin
    pinmode(CLK,OUTPUT);        //SPI clock
    pinmode(GPIO1_CS, OUTPUT);  //GPIO expander 1 chip select
    pinmode(GPIO2_CS, OUTPUT);  //GPIO expander 2 chip select
    pinmode(GPIO3_CS, OUTPUT);  //GPIO expander 3 chip select
    pinmode(GPIO4_CS, OUTPUT);  //GPIO expander 4 chip select
    pinmode(ADC_CS, OUTPUT);    //Analog to digital converter chip select
    pinmode(POT_CS, OUTPUT);    //Digital potentiometer chip select
    pinmode(MISO,INPUT);        //Data input pin
}//initPin

void initState(){
    //Sets the header pins to their initial states (high or low)
    //Deselect all ICs
    digitalWrite(GPIO1_CS, HIGH);
    digitalWrite(GPIO2_CS, HIGH);
    digitalWrite(GPIO3_CS, HIGH);
    digitalWrite(GPIO4_CS, HIGH);
    digitalWrite(ADC_CS, HIGH);
    digitalWrite(POT_CS, HIGH);
    //SPI initial states
    digitalWrite(CLK, LOW);
    digitalWrite(MOSI, LOW);
}//initState

void initGPIO(){
    //Sets the direction for all ICs on the expansion board
    initPin();
    initState();
    initXPNDR(GPIO1_CS);
    initXPNDR(GPIO2_CS);
    initXPNDR(GPIO3_CS);
    initXPNDR(GPIO4_CS);
    
}//initGPIO

void initXPNDR(unsigned char CS){
    /*Assigns register A as all input and register B as all output
      Verify this is acceptable for all GPIOs on the board*/
    unsigned long input = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRA<<8)+ALL_INPUT;
    unsigned long output = (GPIO_OPCODE_WRITE<<16)+(GPIO_SELECT_DIRB<<8)+ALL_OUTPUT;
    struct Message messageA = msgMkr(input,24);
    struct Message messageB = msgMkr(output,24);
    writeSPI(CS,messageA);                                                              //Write Port A configuration over SPI
    writeSPI(CS,messageB);                                                              //Write Port B configuration over SPI
}//initXPNDR


void writeSPI(unsigned char CS, struct Message data){
    digitalWrite(CS, LOW);
    for (int i=0; i<data.length; i++){
        digitalWrite(MOSI,getBit(i,data.word))
        digitalWrite(CLK,HIGH);
        //add sleep function for 0.005 seconds
        digitalWrite(CLK,LOW);
        //add sleep function for 0.005 seconds
    }
    digitalWrite(MOSI, LOW);
    digitalWrite(CS, HIGH);
    //add sleep function for 0.005 seconds
}//writeSPI

unsigned char getBit(unsigned char idx, unsigned char data){
    return (data & (1 << idx)) >> idx
}//getBit

