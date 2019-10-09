#lang racket

(require "env.rkt")
(require "parseB.rkt")

(define eval-exp 
  (lambda (exp env) 
    (cond
      [(lit-exp? exp) (LitValue exp)]
      [(var-ref? exp) (lookup-env env (Symbol exp))]
      [(define-exp? exp) (let ([sym (define-exp-sym exp)]
                               [val (eval-exp (define-exp-exp exp) env)])
                           (do-define sym val))]
      [else (error 'eval-exp  "Invalid symbol: ~s" exp)])))

;What is a valid input and output supposed to look like?

(provide eval-exp)

