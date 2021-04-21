#ifndef UMATT_DEFINITIONS_H_
#define UMATT_DEFINITIONS_H_

//Just in case they're not defined yet
#ifndef	TRUE
#  define	TRUE	(1==1)
#  define	FALSE	(!TRUE)
#endif

#define LOW         0
#define HIGH        1

//FIXME: Currently redefining the I/O from wiringPi.h incorrectly..
#ifndef OUTPUT
#	define OUTPUT		0 		//Verify this is right
#	define INPUT		1
#endif

/*Header pin assignments as per `$gpio readall` on a rpi b3+
 * NOTE* we're using WiringPi pin numbering mode for portability.
 * Pin:| Name      | wPi#  | Phys#  | P20CB# |
 * ----|-----------|-------|--------|--------| */
#define MOSI 		12		//19		10
#define MISO 		13		//21		11
#define CLK  		14		//23		12
#define GPIO1_CS	16		//36		23
#define GPIO2_CS	22		//31		16
#define GPIO3_CS	23		//33		17
#define GPIO4_CS	26		//32		25
#define ADC_CS 		21		//29		15
#define POT_CS		24		//35		18

#endif
