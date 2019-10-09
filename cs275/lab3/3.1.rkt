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