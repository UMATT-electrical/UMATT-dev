#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wiringPi.h>

#include "adc.h"
#include "definitions.h"
#include "init.h"
#include "pot.h"
#include "spi.h"


void printBinary32(uint32_t data) {
    for(int i=31; -1<i; i--) {
		printf("%d", ((data & (1 << i)) >> i));
        if(i%8==0)
            printf("  ");
    }
}

void printBinary8(uint8_t data) {
    for(int i=7; -1<i; i--) {
		printf("%d", ((data & (1 << i)) >> i));
        if(i%8==0)
            printf("  ");
    }
}

/**Changes the direction of the pins to output
 * @param pins[]: Pins to be set as output
 * @param size: Size of param pins[]
 * 
 */ 
void allOutput(uint8_t pins[], uint16_t size){
	for (uint8_t i = 0; i<size; i++){
		pinMode(pins[i],OUTPUT);
	}
}//allOutput

void initBoard(void){
	//Setup wiringPi pin numbering scheme. (run `$gpio readall`)
	if(0 < wiringPiSetup()) {
		printf("WiringPi Setup Failure.");
		exit(EXIT_FAILURE);
	}
	/* Initializes header pins, auxililary chips, and SPI for the drive program	 */
	void initPin(void);		//set direction on header pins
	void initState(void);	//de-select all ICs and clear SPI pins
	void initXPNDR(void);	//configure GPIO expanders
	void initPot(void);		//set potentiometer voltage
}//initBoard

/** Sequentially blinks a bank of SPI pins
 * Useful in testing configurations
 * @param CS: 8bit int defining the ChipSelect line to use
 * @param bank: 16bit int defining ________.
 */
void blinkBank(uint8_t CS, uint16_t bank){
	//Pin is the actual pin on the SPI device (as defined by a bitmask)
	uint8_t pin = 1;
	uint8_t clear = 0;
	//Half a second (in microseconds)
	unsigned int sleepy = 500000;
	printf("****************\n*   Blinking   *\n*\tBank: %d\n*\tCS: %d\n****************\n", bank, CS);
	for (uint8_t i = 0; i<8; i++){
		printf("\t %d: pin=%u\n", i, pin);
		//Force print to console. 
		fflush(stdout);
		writeGPIO(CS, bank, pin);
		usleep(sleepy);
		writeGPIO(CS, bank, clear);
		usleep(sleepy);
		//Shift pin bitmask one to the left
		pin = pin << 1;
	}
}

////////////////////////////////////////////////////////////////////////
///////////////////////////// TESTING MAIN /////////////////////////////
////////////////////////////////////////////////////////////////////////
/**CLI For testing specific pins
 * 
 * Note: You can feed this a text file via piping to stdin 
 *   where each newline is a new command (for automated testing) 
 */ 
void testPins() {
	//Functions include, set, get
	char *inLine = NULL;
	size_t inLength = 0;
	ssize_t inRead = 0;
	int i = 0;
	//Tokens are the command options input
	char *tokens[4] = {NULL, NULL, NULL, NULL};
	
	uint8_t chipSels[] = {GPIO1_CS, GPIO1_CS, GPIO2_CS, GPIO3_CS, GPIO4_CS};
	uint8_t chipSel = 0;
	uint16_t bank = 0;
	uint8_t pin = 1;
	
	
	while(1) {
		printf("I'm not checking any inputs, type correctly or bugger everything up :)\n");
		printf("usage: [get|set] <CS[0-3]> [a|b] <pin#[0-7]>\n");
		inRead = getline(&inLine, &inLength, stdin);
		//Users quit by not entering anything
		if(inRead < 2)
			break;
		//To hell with input checking, user formats incorrectly we crash.
		tokens[0] = strtok(inLine, " ");
		for(i=1; i<4; i++)
			tokens[i] = strtok(NULL, " \n");
			
		for(i=0; i<4; i++)
			printf("[%s], ", tokens[i]);
		printf("\n");
	
		//Get the chip select
		chipSel = chipSels[atoi(tokens[1])];
		//Get the bank
		if(tokens[2][0] == 'a')
			bank = GPIO_SELECT_PORTA;
		else
			bank = GPIO_SELECT_PORTB;
		//Get or set?
		if(tokens[0][0] == 's') {
			//Get the pin number
			pin = 1<<atoi(tokens[3]);
			
			printf("Setting CS:%d bank:%d pin:%s ->", chipSel, bank, tokens[3]);
			printBinary8(pin);
			printf("\n");
			writeGPIO(chipSel, bank, pin);
			sleep(1);
			writeGPIO(chipSel, bank, (uint8_t)0);
		} else {
			printf("Getting CS:%d bank:%d", chipSel, bank);
			pin = readGPIO(chipSel, bank);
			
			printBinary8(pin);
			
			printf("Pin %s set %s", tokens[3], (pin&(1<<atoi(tokens[3])))?"hi":"lo");
		}
		printf("\n");
	}
	free(inLine);
	free(tokens[0]);
	free(tokens[1]);
	free(tokens[2]);
	free(tokens[3]);
}



//int main(int argc, char** argv){
int main(){
	printf("\n\n\n\n\nBegin initilization.\n");
	initBoard();							//set I/O pins to the drive.c configuration
	printf("Init finished\n");
	
	//Currently just setting everything as output, to hell with initBoard();
	//uint8_t pins[] = {MISO, MOSI, CLK, GPIO1_CS, GPIO2_CS, GPIO3_CS, GPIO4_CS};
	//allOutput(pins, 7);
	
	/*Test all 8 pins on banks A,B with CS 1,2,3,4 as outputs.
	blinkBank(GPIO1_CS,GPIO_SELECT_PORTA);
	blinkBank(GPIO1_CS,GPIO_SELECT_PORTB);
	blinkBank(GPIO2_CS,GPIO_SELECT_PORTA);
	blinkBank(GPIO2_CS,GPIO_SELECT_PORTB);
	blinkBank(GPIO3_CS,GPIO_SELECT_PORTA);
	blinkBank(GPIO3_CS,GPIO_SELECT_PORTB);
	blinkBank(GPIO4_CS,GPIO_SELECT_PORTA);
	blinkBank(GPIO4_CS,GPIO_SELECT_PORTB);
	*/
	
	testPins();
	
	printf("Program complete.\n");
}//main
