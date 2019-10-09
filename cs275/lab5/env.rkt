#lang racket

(define empty-env (lambda () (list 'empty-env)))
(define extended-env (lambda (syms vals old-env) (list 'extended-env syms vals old-env)))

(define empty-env? (lambda (x)
      (cond
            [(not (pair? x)) #f]
            [else (eq? (car x) 'empty-env)])))

(define extended-env? (lambda (x)
      (cond
            [(not (pair? x)) #f]
            [else (eq? (car x) 'extended-env)])))

(define environment? (lambda (x) (or (empty-env? x) (extended-env? x))))

(define syms (lambda (env)
     (cond
           [(extended-env? env) (cadr env)]
           [else (error 'syms "bad environment")])))


(define vals (lambda (env)
      (cond
            [(extended-env? env) (caddr env)]
            [else (error 'vals "bad environment")])))


(define old-env (lambda (env)
     (cond
           [(extended-env? env) (cadddr env)]
           [else (error 'old-env "bad environment")])))

(define the-empty-env (empty-env))

(define EnvA (extended-env '(x y) '(1 2) the-empty-env))
(define EnvB (extended-env '(x z) '(5 7) EnvA))

(define lookup-env
  (lambda (env sym)
    (if (empty-env? env) (error 'apply-env "No binding for ~s" sym)
        (let([symbols (syms env)]
             [values (vals env)])
          (let([f (lambda(symbol value)
               (cond
                 [(eq? (car symbol) sym) (car value)]
                 [(eq? (cadr symbol) sym) (cadr value)]
                 [else (lookup-env (old-env env) sym)]))])
            (f symbols values))))))

(define init-env (extended-env '(x y) '(10 23) the-empty-env))

(provide empty-env extended-env empty-env? extended-env? syms vals old-env the-empty-env EnvA EnvB lookup-env init-env)

