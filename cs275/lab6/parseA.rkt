#lang racket
(require "env.rkt")
(define parse
  (lambda (input)
    (expression input)))

(define expression
  (lambda (input)
    (cond
      [(number? input) (new-lit-exp input)]
      [else (error 'expression "Invalid syntax ~s" input)])))

(define new-lit-exp
  (lambda (input)
    (extended-env '(number) input the-empty-env)))

;(define init-env
 ; (lambda (input)
  ;  (extended-env '(number) input the-empty-env)))

(define lit-exp?
  (lambda (env)
    (if (extended-env? env) #t #f)))

(define LitValue
  (lambda (tree)
    (if (lit-exp? tree) (caddr tree) (error 'eval-exp "Invalid tree: ~s" tree))))

(provide parse expression new-lit-exp lit-exp? LitValue)