OVERVIEW
========

This module was created to supplement Python's itertools module, filling in gaps
in two important areas of basic combinatorics:

(A) ordered and unordered m-way combinations, and
(B) generalizations of the four basic occupancy problems ('balls in boxes').

Brief descriptions of the included functions and classes follow (more detailed
descriptions and additional examples can be found in the individual doc strings
within the functions):

n_choose_m(n, m): calculate n-choose-m, using a simple algorithm that is less
likely to involve large integers than the direct evaluation of n! / m! / (n-m)!

m_way_ordered_combinations(items, ks): This function returns a generator that
produces all m-way ordered combinations (multinomial combinations) from the
specified collection of items, with with ks[i] items in the ith group, i= 0, 1,
2, ..., m-1, where m= len(ks) is the number of groups. By 'ordered
combinations', we mean that the relative order of equal- size groups is
important; the order of the items within any group is not important. The total
number of combinations generated is given by the multinomial coefficient formula
(see http://en.wikipedia.org/wiki/Multinomial_theorem#Multinomial_coefficients).

m_way_unordered_combinations(items, ks): This function returns a generator that
produces all m-way unordered combinations from the specified collection of
items, with ks[i] items in the ith group, i= 0, 1, 2, ..., m-1, where m= len(ks)
is the number of groups. By 'unordered combinations', we mean that the relative
order of equal-size groups is not important. The order of the items within any
group is also unimportant.

Example of ``m_way_unordered_combinations``:

.. code::

   Issue the following statement from the IPython prompt:

   from combinatorics import *
   list(m_way_unordered_combinations(6,[2,2,2]))

   The output consists of the 15 combinations listed below:

   (0, 1), (2, 3), (4, 5)
   (0, 1), (2, 4), (3, 5)
   (0, 1), (2, 5), (3, 4)
   (0, 2), (1, 3), (4, 5)
   (0, 2), (1, 4), (3, 5)
   (0, 2), (1, 5), (3, 4)
   (0, 3), (1, 2), (4, 5)
   (0, 3), (1, 4), (2, 5)
   (0, 3), (1, 5), (2, 4)
   (0, 4), (1, 2), (3, 5)
   (0, 4), (1, 3), (2, 5)
   (0, 4), (1, 5), (2, 3)
   (0, 5), (1, 2), (3, 4)
   (0, 5), (1, 3), (2, 4)
   (0, 5), (1, 4), (2, 3)

unlabeled_balls_in_labeled_boxes(balls, box_sizes): This function returns a
generator that produces all distinct distributions of indistinguishable balls
among labeled boxes with specified box sizes (capacities). This is a
generalization of the most common formulation of the problem, where each box is
sufficiently large to accommodate all of the balls, and is an important example
of a class of combinatorics problems called 'weak composition' problems.

unlabeled_balls_in_unlabeled_boxes(balls, box_sizes): This function returns a
generator that produces all distinct distributions of indistinguishable balls
among indistinguishable boxes, with specified box sizes (capacities). This is a
generalization of the most common formulation of the problem, where each box is
sufficiently large to accommodate all of the balls. It might be asked, 'In what
sense are the boxes indistinguishable if they have different capacities?' The
answer is that the box capacities must be considered when distributing the
balls, but once the balls have been distributed, the identities of the boxes no
longer matter.

Example of ``unlabeled_balls_in_unlabeled_boxes``:

.. code::

   Issue the following commands from the IPython prompt:

   from combinatorics import *
   list(unlabeled_balls_in_unlabeled_boxes(10,[5,4,3,2,1]))

   The output is as follows:

   [(5, 4, 1, 0, 0),
    (5, 3, 2, 0, 0),
    (5, 3, 1, 1, 0),
    (5, 2, 2, 1, 0),
    (5, 2, 1, 1, 1),
    (4, 4, 2, 0, 0),
    (4, 4, 1, 1, 0),
    (4, 3, 3, 0, 0),
    (4, 3, 2, 1, 0),
    (4, 3, 1, 1, 1),
    (4, 2, 2, 2, 0),
    (4, 2, 2, 1, 1),
    (3, 3, 3, 1, 0),
    (3, 3, 2, 2, 0),
    (3, 3, 2, 1, 1),
    (3, 2, 2, 2, 1)]

labeled_balls_in_unlabeled_boxes(balls, box_sizes): This function returns a
generator that produces all distinct distributions of distinguishable balls
among indistinguishable boxes, with specified box sizes (capacities). This is a
generalization of the most common formulation of the problem, where each box is
sufficiently large to accommodate all of the balls.

labeled_balls_in_labeled_boxes(balls, box_sizes): This function returns a
generator that produces all distinct distributions of distinguishable balls
among distinguishable boxes, with specified box sizes (capacities). This is a
generalization of the most common formulation of the problem, where each box is
sufficiently large to accommodate all of the balls.

Example of ``labeled_balls_in_labeled_boxes``:

.. code::

   Issue the following statements from the IPython prompt:

   from combinatorics import *
   list(labeled_balls_in_labeled_boxes(3,[2,2]))

   The output is as follows:

   [((0, 1), (2,)),
    ((0, 2), (1,)),
    ((1, 2), (0,)),
    ((0,), (1, 2)),
    ((1,), (0, 2)),
    ((2,), (0, 1))]

partitions(n): 'In number theory and combinatorics, a partition of a positive
integer n, also called an integer partition, is a way of writing n as a sum of
positive integers. Two sums that differ only in the order of their summands are
considered to be the same partition.'  We can trivially generate all partitions
of an integer using ``unlabeled_balls_in_unlabeled_boxes``.  The quote is from
http://en.wikipedia.org/wiki/Partition_(number_theory) .


AUTHOR
======

Dr. Phillip M. Feldman

Comments and suggestions--especially bug reports--can be communicated to me via
the following e-mail address: Phillip.M.Feldman@gmail.com




Credits
-------

- `Distribute`_
- `Buildout`_
- `modern-package-template`_

.. _Buildout: http://www.buildout.org/
.. _Distribute: http://pypi.python.org/pypi/distribute
.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template
