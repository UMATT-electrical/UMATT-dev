#ifndef ADC_H
#define ADC_H

#define ADC_CH0 	0b1000
#define ADC_CH1 	0b1001
#define ADC_CH2 	0b1010
#define ADC_CH3 	0b1011
#define ADC_CH4 	0b1100
#define ADC_CH5 	0b1101
#define ADC_CH6 	0b1110
#define ADC_CH7 	0b1111
#define RESOLUTION	12
#define OPCODE_SIZE	5

uint16_t readADC(uint8_t channel);

#endif
