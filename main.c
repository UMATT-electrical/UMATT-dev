#include <wiringPi.h>
//#include <stdio.h>
#include <stdint.h>
#include "definitions.h"
#include "init.h"
#include "spi.h"
#include "adc.h"
#include "pot.h"

void main(void){
	void initPin(void);		//set direction on header pins
	void initState(void);	//de-select all ICs and clear SPI pins
	void initXPNDR(void);	//configure GPIO expanders
	void initPot(void);		//set potentiometer voltage
}
