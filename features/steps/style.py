from behave import *
import numpy
import toyplot.testing

@given(u'a sample plot, the plot can be rendered with a dashed line style.')
def step_impl(context):
    canvas, axes, mark = toyplot.plot(numpy.linspace(0, 1) ** 2, style={"stroke-dasharray":"5,5"})
    toyplot.testing.assert_canvas_equal(canvas, "style-stroke-dasharray")