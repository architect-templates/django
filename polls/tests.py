import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question

# Create your tests here.

def create_question(question_text, days):
  """
  Create a question with the given `question_text` and pulished the
  given number of `days` offset to now(negative for questions
  published in the past, positive for questions that have yet to be published).
  """
  time = timezone.now() + datetime.timedelta(days=days)
  return Question.objects.create(question_text=question_text, pub_date=time)

def create_choice(question_text, days, choice_text=0):
  """
  Createing a question and choice with giver informations
  """
  question = create_question(question_text, days)
  if choice_text:
    question.choice_set.create(choice_text=choice_text, votes=0)
    return question
  else:
    return question

class QuestionIndexViewTests(TestCase):
  def test_no_questions(self):
    """
    If no questions exist, an appropriate message is displayed.
    """
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available.")
    self.assertQuerysetEqual(response.context['latest_question_list'], [])

  def test_past_question(self):
    """
    Questions with a pub_date in the past are displayed on the
    index page.
    """
    question = create_question(question_text="Past question.", days=-30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      [question],
    )

  def test_future_question(self):
    """
    Questions with a pub_date in the future aren't displayed on
    the index page.
    """
    create_question(question_text="Future question.", days=30)
    response = self.client.get(reverse('polls:index'))
    self.assertContains(response, "No polls are available.")
    self.assertQuerysetEqual(response.context['latest_question_list'], [])

  def test_future_question_and_past_question(self):
    """
    Even if both past and future questions exist, only past questions
    are displayed.
    """
    question = create_question(question_text="Past question.", days=-30)
    create_question(question_text="Future question.", days=30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      [question],
    )

  def test_two_past_questions(self):
    """
    The questions index page may display multiple questions.
    """
    question1 = create_question(question_text="Past question 1.", days=-30)
    question2 = create_question(question_text="Past question 2.", days=-5)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      [question2, question1],
    )

  def test_no_choice(self):
    """
    Will rise a 404 not found if the question hadnt any choice.
    """
    no_choice = create_choice(question_text="No Choice.", days=-2)
    url = reverse('polls:result', args=(no_choice.id,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)

  def test_with_choice(self):
    """
    Will show the choice_text if thers was some.
    """
    question = create_choice(question_text='With Choice.', days=-2,
    choice_text='With Choice')
    url = reverse('polls:result', args=(question.id,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

class QuestionDetailViewTests(TestCase):
  def test_future_question(self):
    """
    The detail view of a question with a pub_date in the future
    returns a 404 not found.
    """
    future_question = create_question(question_text='Future question.', days=5)
    url = reverse('polls:detail', args=(future_question.id,))
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)

  def test_past_question(self):
    """
    The detail view of a question with a pub_date in the past
    displays the question's text.
    """
    past_question = create_question(question_text='Past Question.', days=-5)
    url = reverse('polls:detail', args=(past_question.id,))
    response = self.client.get(url)
    self.assertContains(response, past_question.question_text)
