/* -- n_squared.s */
.data
.balign 4										@ First message
message1: .asciz "Escribe un numero: "
.balign 4
message2: .asciz "La suma de cuadrados con n = %d es %d\n"
.balign 4
message3: .asciz "N es muy grande, usa otro numero"
.balign 4										@ Format pattern for scanf
scan_pattern: .asciz "%d"
.balign 4										@ Where scanf will store the number read
number_read: .word 0
.balign 4
return: .word 0

.text    
.global main
main:
    ldr r1, =return 			@ r1 <- &return
    str lr, [r1] 				@ *r1 <- lr
    ldr r0, =message1 			@ r0 <- &message1
    bl printf 					@ call to printf
    ldr r0, =scan_pattern 		@ r0 <- &scan_pattern
    ldr r1, =number_read 		@ r1 <- &number_read
    bl scanf 					@ call to scanf
    
    ldr r1, =number_read 		@ r1 <- &number_read
    ldr r1, [r1] 				@ r1 <- *r1
    
    cmp r1, #1024 				@ compare r1 and 1024 (in reality, 1860 is the max)
    bgt error    				@ branch if r1 > 1024 to display an error message
 
    mov r2, #0 					@ r2 <- #0 (initialize sum)
    mov r4, #1 					@ r4 <- #1 (counter to check if n has been reached)
   
loop:
    cmp r4, r1 					@ compare r4 and r1 (n)
    bgt success 				@ branch to success if r4 > r1
    mul r3, r4, r4		 		@ r3 <- r4 * r4
    add r2, r2, r3		 		@ r2 <- r2 + r3
    add r4, r4, #1 				@ r4 <- r4 + 1
    b loop
    
success:
    ldr r0, =message2 			@ r0 <- &message2
    ldr r1, =number_read 		@ r1 <- &number_read
    ldr r1, [r1] 				@ r1 <- *r1
    bl printf 					@ call to printf
    b end
    
error:
    ldr r0, =message3 			@ r0 <- &message3
    bl printf 					@ call to printf
    
end:
    bx lr 						@ return from main using lr
    
/* External */
.global printf
.global scanf
