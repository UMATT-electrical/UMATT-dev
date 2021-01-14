unsigned char readADC(unsigned char channel){
    unsigned char data;
    struct Message message = msgMkr(channel, 6);//ADC requires leading zeros
    writeSPI(ADC_CS, message);
    return ADCreader(ADC_CS);
}//readGPIO

unsigned char ADCreader(void){
    unsigned char data;
    digitalWrite(ADC_CS, LOW);
    for (int i=0; i<12; i++){
         digitalWrite(CLK,HIGH);
         //add sleep function for 0.005 seconds
        data = data<<1 + digitalRead(MISO);
        digitalWrite(CLK,LOW);
        //add sleep function for 0.005 seconds
    }
    digitalWrite(ADC_CS, HIGH);
    return data;
}//ADCreader
