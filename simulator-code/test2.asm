add $s1,$s2,$s3
add $s2, $s1, $s3
li $s2,4
bne $s1,$s2,label
li $t0,4
li $t4,7
label:
li $s3,7
add $s0,$s2,$s3
