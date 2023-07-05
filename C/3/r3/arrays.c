/* SYSC 2006 Lab 3. 

 * Incomplete implementations of the functions that will be coded during the lab.
 */

#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#include "arrays.h"

/* Exercise 1. */

/* Return the average magnitude of the signal represented by
 * the n doubles in x[]. 
 * This function assumes that parameter n is >= 1.
 */
double avg_magnitude(double x[], double n)
{
	double sum = 0;
    for(int i = 0; i < n; i++){
		sum = fabs(x[i]) + sum;
		}
	return sum/n;
}

/* Exercise 2. */

/* Return the average power of the signal represented by
 * the n doubles in x[].
 * This function assumes that parameter n is >= 1.
 */
double avg_power(double x[], double n)
{
	double sum = 0;
    for(int i = 0; i < n; i++){
		sum = fabs(x[i])*fabs(x[i]) + sum;
		}
	return sum/n;
}

/* Exercise 3. */

/* Return the largest of the n doubles in arr[]. 
 * This function assumes that parameter n is >= 1.
 */
double max(double arr[], int n)
{
	double mv = arr[0];
	for(int i = 0; i < n; i++){
		if(mv<arr[i]){
			mv= arr[i];
			};
		}
    return mv;
}

/* Exercise 4. */

/* Return the smallest of the n doubles in arr[]. 
 * This function assumes that parameter n is >= 1.
 */
double min(double arr[], int n)
{
	double mv = arr[0];
	for(int i = 0; i < n; i++){
		if(mv > arr[i]){
			mv= arr[i];
			};
		}
    return mv;
}

/* Exercise 5. */

/* Normalize the n doubles in x[]. 
 * This function assumes that parameter n is >= 2, and that at least
 * two of the values in x[] are different.
 */
void normalize(double x[], int n)
{
	double mn = min(x,n);
	double mx = max(x,n);
	for(int i = 0; i < n; i++){
		x[i] = (x[i]-mn)/(mx-mn);
		}
}
