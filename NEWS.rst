.. This is your project NEWS file which will contain the release notes.
.. Example: http://www.python.org/download/releases/2.6/NEWS.txt
.. The content of this file, along with README.rst, will appear in your
.. project's PyPI page.

REVISION HISTORY
================

08-28-2012, version 1.4.1, Phillip M. Feldman:

(minor) I implemented a bug fix in ``off_by_m_algorithm3``: One must copy the
result before yielding it to the calling program; otherwise, the same object is
being re-used.  This bug fix was contributed by Corran Webster of Enthought.


08-26-2012, version 1.4.0, Phillip M. Feldman:

(minor/intermediate) I added three algorithms that solve the off-by-m problem.
The first, which is the slowest, and the last, which is the fastest, were
written by me.  The second was contributed by Warren Weckesser of Enthought.


08-10-2012, version 1.3.0, Phillip M. Feldman:

(minor+) I incorporated a patch contributed by David Hollman
(david.s.hollman@gmail.com).  This patch corrects a serious flaw in the
generator function ``_m_way_unordered_combinations``, which is used by
``m_way_unordered_combinations`` and by ``labeled_balls_in_unlabeled_boxes``.
Without the patch, ``labelled_balls_in_unlabeled_boxes`` misses some valid
combinations.

(minor/intermediate) I added the function ``off_by_one``, which returns a
generator that enumerates all possible solutions of the 'off-by-one' problem.


04-06-2012, version 1.2.0, Phillip M. Feldman:

I added the function ``prod``, which is similar to ``numpy.prod`` but does all
calculations using large arithmetic when operating on a sequence of integers.

I fixed a bug in ``n_choose_m``: We must force the division to be done using
integer arithmetic because otherwise Python attempts to convert the results from
``prod`` into floating point numbers, which can fail for n greater than 170.

I added the function ``n_choose_m_ln``.  This function calculates the natural
logarithm of choose(n,m), defined as the number of ways in which one can select
m of n distinct objects without regard for order, using SciPy's ``gammaln``
function.  For large n, especially for n > 10000, this function is much faster
than ``n_choose_m`` (computational and memory requirements are both much lower).


10-09-2011, version 1.1.1, Phillip M. Feldman:

I added a function to generate partitions.


10-01-2011, version 1.1.0, Phillip M. Feldman:

I added input error checking to the ``labeled_balls_in_unlabeled_boxes`` function.

I fixed the function ``m_way_ordered_combinations`` so that the box order
specified via the input argument ``ks`` is respected.

I added the function ``labeled_balls_in_labeled_boxes``.  This completes the basic
set of functions for solving occupancy functions with capacity limits.

09-24-2011: Initial version.

