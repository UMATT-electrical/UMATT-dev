#ifndef UMATT_SPI_H_
#define UMATT_SPI_H_

#include <unistd.h>
#include <stdint.h>
#include <stdio.h>
#include <time.h>
#include "definitions.h"
#include "wiringPi.h"




typedef struct Message_32b {
   uint32_t operation; 	//message to be sent over SPI
   uint8_t 	length;		//message length
} message_32b;//Message_32b

message_32b msgMkr(uint32_t data, uint8_t size);
void writeSPI(uint8_t CS, struct Message_32b data);
uint8_t getBit(uint8_t idx, uint32_t data);
uint16_t readSPI(uint8_t CS, uint8_t length);

#endif
