/**
 * DRIVE_C
 * @author K Gledson
 * @version 2021-01-20
 *
 */

void initDrive(void){
	/*Initializes Raspberry Pi header pins and auxiliary chips
	 *
	 */
	void initPin(void);		//set direction on header pins
	void initState(void);	//de-select all ICs and clear SPI pins
	void initXPNDR(void);	//configure GPIO expanders
	void initPot(void);		//set potentiometer voltage
}//initDrive

void run(void){
	initDrive();
}//run


