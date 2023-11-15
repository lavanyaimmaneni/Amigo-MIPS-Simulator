.data
.text
.globl main
main:
  # loading values randomly
  # u can change the order
  li $s0,8
  li $s1,7
  li $s2,6
  li $s3,5
  li $s4,4
  # sorting begins

  slt $s0,$s1,label1
  addi $t0,$s1,0
  addi $s1,$s0,0
  addi $s0,$t0,0
label1:
 slt $s0,$s2,label2
 addi $t0,$s2,0
 addi $s2,$s0,0
 addi $s0,$t0,0
label2:
 slt $s0,$s3,label3
 addi $t0,$s3,0
 addi $s3,$s0,0
 addi $s0,$t0,0
label3:
 slt $s0,$s4,label4
 addi $t0,$s4,0
 addi $s4,$s0,0
 addi $s0,$t0,0
label4:
 slt $s1,$s2,label5
 addi $t0,$s2,0
 addi $s2,$s1,0
 addi $s1,$t0,0
label5:
 
 slt $s1,$s3,label6
 addi $t0,$s3,0
 addi $s3,$s1,0
 addi $s1,$t0,0
label6:
 
 slt $s1,$s4,label7
 addi $t0,$s4,0
 addi $s4,$s1,0
 addi $s1,$t0,0
label7:
 slt $s2,$s3,label8
 addi $t0,$s3,0
 addi $s3,$s2,0
 addi $s2,$t0,0
label8:
 slt $s2,$s4,label9
 addi $t0,$s4,0
 addi $s4,$s2,0
 addi $s2,$t0,0
label9:
 slt $s3,$s4,exit
 addi $t0,$s4,0
 addi $s4,$s3,0
 addi $s3,$t0,0
# sorting ends
# see updated registers values in registers coulmn
exit:
