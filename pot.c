void writePot(unsigned char value){
    unsigned long word = (POT_OPCODE_WRITE<<12)+(POT_SELECT_0<<8)+value;
    struct Message message = msgMkr(word,16);
    writeSPI(POT_CS,message);
}//writePot

void setPot(unsigned char value){
    value = getMax(0, getMin(1,1-value)); //idk why this is a thing
    writePot(value);
}

unsigned char getMax (unsigned char xx, unsigned char yy){
    unsigned char max = yy;
    if (xx > yy){
        max = xx;
    }
    return max;
}//getMax

unsigned char getMin(unsigned char xx, unsigned char yy){
    unsigned char min = yy;
    if (xx < yy){
        min = xx;
    }
    return min;
}//getMin
