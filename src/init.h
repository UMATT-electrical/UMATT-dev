#ifndef UMATT_INIT_H_
#define UMATT_INIT_H_

#include <stdint.h>
#include <wiringPi.h>

#include "definitions.h"
#include "gpio.h"
#include "pot.h"

void initPin(void);
void initState(void);
void initXPNDR(void);
void initPot(void);

#endif
