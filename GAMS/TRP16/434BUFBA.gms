*************************************************************
**********FLUX BALANCE ANALYSIS FOR CHLAMYDIA****************
*************************************************************
*****************Niaz Bahar Chowdhury************************
*************************************************************
$INLINECOM /*  */

OPTIONS

	limrow = 1000
       	optCR = 0
        optCA = 0
        iterlim = 100000
        decimals = 7
        reslim = 100000
        work = 5000000;

*********Defining Sets**************************************
SETS

	i					set of metabolites

$include "metabolites.txt"	

	j					set of reactions

$include "reactions.txt"

;
*************************************************************

***********Defining Parameters*******************************
PARAMETERS

	S(i,j)					stoichiometric matrix

$include "sij.txt"

	v_max(j)				maximum flux of v(j)
	
$include "upper_bound.txt"

	v_min(j)				minimum flux of v(j)

$include "lower_bound.txt"
;
**************************************************************

*********Defining Equations***********************************
EQUATIONS

	objective				objective function
	mass_balance(i)				steady state mass balance
	lower_bound(j)				lower bounds on reactions
	upper_bound(j)				upper bounds on reactions
;
**************************************************************

*********Defining Variables***********************************
FREE VARIABLES

	v(j)					reaction flux
	Z					objective value
;

****************************************************************

***************Defining Model***********************************
objective..			Z =e= v('bio1_biomass');

mass_balance(i)..		sum(j, S(i,j) * v(j)) =e= 0;

lower_bound(j)..		v_min(j) =l= v(j);

upper_bound(j)..		v(j) =l= v_max(j);

Model chlamydia_FBA /all/;
******************************************************************

**********Solving Model*********************

chlamydia_FBA.holdfixed = 1;

solve chlamydia_FBA using lp maximizing Z;
********************************************
****************Output File*****************
FILE RESULTS /CHLAMYDIA_FBA.txt/;

PUT RESULTS;

PUT "reaction      FLUX"/;

LOOP(j,
	
	PUT j.tl:0:100,"    ", v.l(j):20:8/;
		
);

PUTCLOSE;
**********************************************