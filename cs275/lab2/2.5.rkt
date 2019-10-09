#lang racket
(define phone-book 
         '( (barbara 775-1234) (luke 774-2839) (nick 775-0912) (valerie 775-9043) ))

(define phone-number
  (lambda (person phone-book)
    (cond
      [(null? phone-book) 'disconnected]
      [(eq? person (car (car phone-book))) (cadr (car phone-book))]
      [else (phone-number person (cdr phone-book))])))