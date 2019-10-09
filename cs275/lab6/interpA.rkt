#lang racket

(require "env.rkt")
(require "parseA.rkt")

(define eval-exp 
  (lambda (tree env) 
    (cond
      [(lit-exp? tree) (LitValue tree)]
      [else (error 'eval-exp  "Invalid tree: ~s" tree)])))

(provide eval-exp)