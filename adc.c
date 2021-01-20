/**
 * ADC_C
 * @author K Gledson
 * @version 2021-01-20
 *
 */

unsigned char readADC(unsigned char channel){
	/*	reads the specified ADC channel
	 * 	returns the ADC data
	 */
    struct Message message = msgMkr(channel, 6); 	//ADC requires leading zeros
    writeSPI(ADC_CS, message);						//Request transmission from ADC
    return ADCreader(ADC_CS);						//Return ADC transmission
}//readGPIO

unsigned char ADCreader(void){
    unsigned char data;							//Data from transmission
    digitalWrite(ADC_CS, LOW);					//Select ADC chip
    for (int i=0; i<RESOLUTION; i++){			//Begin SPI communication
         digitalWrite(CLK,HIGH);				//Set clock high
         //add sleep function for 0.005 seconds
        data = data<<1 + digitalRead(MISO);		//Append new bit to data
        digitalWrite(CLK,LOW);					//Set clock low
        //add sleep function for 0.005 seconds
    }
    digitalWrite(ADC_CS, HIGH);					//Deselect ADC chip
    return data;
}//ADCreader
