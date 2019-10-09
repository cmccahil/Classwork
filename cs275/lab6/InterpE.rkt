#lang racket

(require "env.rkt")
(require "parseE.rkt")

(define eval-exp 
  (lambda (exp env) 
    (cond
      [(lit-exp? exp) (LitValue exp)]
      [(var-ref? exp) (lookup-env env (Symbol exp))]
      [(define-exp? exp) (let ([sym (define-exp-sym exp)]
                               [val (eval-exp (define-exp-exp exp) env)])
                           (do-define sym val))]
      [(app-exp? exp) (apply-proc (eval-exp (cadr exp) env) (map (lambda (t)(eval-exp t env)) (caddr exp)))] ;evaluate the cadr (procedure) in the environment
      [(if-exp? exp) (if (eval-exp (cadr exp) env) (eval-exp (caddr exp) env) (eval-exp (cadddr exp) env))]
      [(let-exp? exp) (eval-exp (cadddr exp) (do-define (cadr exp) (caddr exp)))]
      [else (error 'eval-exp  "Invalid symbol: ~s" exp)])))

;[else (lookup-env env exp)])))
;What is a valid input and output supposed to look like?
;map eval-exp onto list of arguments

(provide eval-exp)