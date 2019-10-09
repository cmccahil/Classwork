#lang racket

(require "streams.rkt")
(require "keyboard.rkt")

(define IntsFrom$ (lambda (n) (cons$ n (IntsFrom$ (+ n 1)))))

(define Ints$ (IntsFrom$ 0))

(define Evens$ (map$ (lambda (x) (* 2 x))  Ints$))

(define Ones$ (cons$ 1 Ones$))

(define Odds$ (+$ Evens$ Ones$))

(define Ints1$ (cons$ 1 (+$ Ones$ Ints1$)))

(define rember-all$
  (lambda (x s)
    (cond
      [(eqv? x (car$ s)) (rember-all$ x (cdr$ s))]
      [else (cons$ (car$ s) (rember-all$ x (cdr$ s)))])))

(define subst-all$
  (lambda (x y s)
    (cond
      [(eqv? x (car$ s)) (cons$ y (subst-all$ x y (cdr$ s)))]
      [else (cons$ (car$ s) (subst-all$ x y (cdr$ s)))])))

(define pairsFrom$
     (lambda (p)
          (cons$ p (pairsFrom$ (nextPair p)))))

(define pairs$ (pairsFrom$ (cons 1 1)))

(define nextPair
  (lambda (p)
    (cond
      [(eqv? 1 (cdr p)) (cons 1 (+ (car p) 1))]
      [else (cons (+ (car p) 1) (- (cdr p) 1))])))

(define merge$
  (lambda (s1 s2)
    (cond
      [(eqv? (car$ s1) (car$ s2)) (cons$ (car$ s1) (merge$ (cdr$ s1) (cdr$ s2)))]
      [(> (car$ s1) (car$ s2)) (cons$ (car$ s2) (merge$ s1 (cdr$ s2)))]
      [else (cons$ (car$ s1) (merge$ (cdr$ s1) s2))])))

(define scale$
  (lambda (s n)
    (cons$ (* (car$ s) n) (scale$ (cdr$ s) n))))

;(define S
 ; (cons$ 1 (scale$ (IntsFrom$ 1) 2)))

(define S
  (cons$ 1 (merge$ (merge$ (scale$ S 2) (scale$ S 3)) (scale$ S 5))))

(define fact-stream$    
     (cons$ 1 (*$ fact-stream$ (IntsFrom$ 1))))

(define *$ (lambda (s1 s2) (cons$ (* (car$ s1) (car$ s2)) (*$ (cdr$ s1) (cdr$ s2)))))

(define PartialSums$
  			(lambda (s)
    				(cons$ (car$ s) (+$ (PartialSums$ s) (cdr$ s)))))

(define Alt-zeros-ones$
  (cons$ 0 (cons$ 1 (cons$ 0 (cons$ -1 Alt-zeros-ones$)))))

(define Alt-ones-zeros$
  (cons$ 1 (cons$ 0 (cons$ -1 (cons$ 0 Alt-ones-zeros$)))))

(define e-series$ (map$ (lambda (x) (/ 1.0 x)) fact-stream$))

(define sin-series$
  (*$ Alt-zeros-ones$ e-series$))

(define cos-series$
  (*$ Alt-ones-zeros$ e-series$))

(define Powers$ (lambda(x) (cons$ 1 (map$ (lambda (t) (* x t)) (Powers$ x)))))
(define E (lambda (x) (PartialSums$ (*$ (Powers$ x) e-series$))))
(define sin (lambda(x)(PartialSums$ (*$ (Powers$ x) sin-series$))))
(define cos (lambda (x) (PartialSums$ (*$  (Powers$ x) cos-series$))))

(define grune-a-b
  (lambda (s)
    (cond
      [(empty-stream? s) 'the-empty-stream]
      [(eq? 'a (car$ s)) (let grune2 ([f (car$ (keyboard-stream))])
                           (if (eq? 'a f) (cons$ 'b (grune-a-b (cdr$ s))) (cons$ 'a (cons$ f (grune-a-b (cdr$ s))))))]
      [else (cons$ (car$ s) (grune-a-b (cdr$ s)))])))

(define grune
  (lambda (a b)
    (lambda (s)
      (cond
      [(empty-stream? s) 'the-empty-stream]
      [(eq? a (car$ s)) (let ([f (car$ (cdr$ s))])
                           (if (eq? a f) (cons$ b ((grune a b) (cdr$ (cdr$ s)))) (cons$ a (cons$ f ((grune a b) (cdr$ (cdr$ s)))))))]
      [else (cons$ (car$ s) ((grune a b) (cdr$ s)))]))))







