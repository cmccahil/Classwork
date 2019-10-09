#lang racket
(define atom? (lambda (x)
                (not (list? x))))

(define index
  (lambda (a lat)
    (if (boolean? (index-of lat a)) -1 (foldr (lambda (x y)
                                          (if (equal? x a) 0 (+ 1 y)))
                                        0 lat))))
                                          
(define replace
  (lambda (a b lat)
    (foldr (lambda(x y)
            (if (equal? x a) (cons b y) (cons x y)))
          null lat)))

(define bags '((duffle 8) (garment-bag 2) (briefcase 5) (valise 7) (steamer-trunk 65)))

(define sublist
  (lambda (lat)
    (cond
      [(null? lat) null]
      [else (cons (cadr (car lat)) (sublist (cdr lat)))])))

(define weigh
  (lambda (bags)
    (foldr + 0 (sublist bags))))

(define max
  (letrec([max-a (lambda (lat acc)
                   (cond
                     [(null? lat) acc]
                     [(> (cadr (car lat)) (cadr acc)) (max-a (cdr lat) (car lat))]
                     [else (max-a (cdr lat) acc)]))])
    (lambda (lat) (max-a lat '(null 0)))))
    
(define heaviest
  (lambda (bags)
    (foldr (lambda (x y)
             (if (= (cadr x) (cadr (max bags))) (car x) y))
           null bags)))
             
                                     