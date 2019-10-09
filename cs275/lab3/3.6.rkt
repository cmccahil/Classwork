#lang racket

(define firsts
  (lambda (llyst)
    (cond
      ((null? llyst) null)
      (else (cons(car (car llyst)) (firsts (cdr llyst)))))))

(define rests
  (lambda (llyst)
    (cond
      ((null? llyst) null)
      (else (cons(cdr (car llyst)) (rests (cdr llyst)))))))

(define transpose
  (lambda (mat)
    (cond
      [(null? (car mat)) null]
      [else (cons(firsts mat) (transpose (rests mat)))])))

(define dot-product
  (lambda (vec1 vec2)
    (cond
      ((null? vec1) 0)
      (else (apply + (map * vec1 vec2))))))

(define helper
  (lambda(mat1 mat2)
    (cond
      ((null? mat2) null)
      (else (cons(dot-product mat1 (car mat2)) (helper mat1 (cdr mat2)))))))

(define matmult
  (lambda (mat1 mat2)
    (cond
      ((null? mat1) null)
      (else (cons(helper (car mat1) (transpose mat2)) (matmult (cdr mat1) mat2))))))

