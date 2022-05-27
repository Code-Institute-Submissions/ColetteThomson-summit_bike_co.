from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
# 'httpResponseRedirect' to reload template (article_content)
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Article
from .forms import OpinionForm


class ArticleList(generic.ListView):
    """ list of articles on Biketalk """
    model = Article
    # filter contents of article table by '1' (published) by ascending date
    queryset = Article.objects.filter(status=1).order_by('created_on')
    # to render html view
    template_name = 'article_list.html'
    # number of posts that appear on front page
    paginate_by = 2


class ArticleContent(View):
    """ detail of individual articles on Biketalk """
    # get details of article

    def get(self, request, slug, *args, **kwargs):
        """ filter for active articles """
        queryset = Article.objects.filter(status=1)
        # use unique slug to get published article
        article = get_object_or_404(queryset, slug=slug)
        # get post's approved opinions in descending date order
        opinions = article.opinions.filter(approved=True).order_by
        ('-created_on')
        # determine if logged-in user has liked article or not
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        # combine template with context dict for article with liked opinions
        return render(
            request,
            "biketalk/article_content.html",
            {
                "article": article,
                "opinions": opinions,
                # to tell user their opinion is awaiting approval
                "opinioned": False,
                "liked": liked,
                "opinion_form": OpinionForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ filter for active articles """
        queryset = Article.objects.filter(status=1)
        # use unique slug to get published article
        article = get_object_or_404(queryset, slug=slug)
        # get article's approved opinions in descending date order
        opinions = article.opinions.filter(approved=True).order_by
        ('-created_on')
        # determine if logged-in user has liked article or not
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        # obtain all posted form data
        opinion_form = OpinionForm(data=request.POST)

        if opinion_form.is_valid():
            # obtain email and name from logged in user details
            opinion_form.instance.email = request.user.email
            opinion_form.instance.name = request.user.username
            # save form
            opinion = opinion_form.save(commit=False)
            # determine which article an opinion has been left and save
            opinion.article = article
            opinion.save()
            # display success message to user
            messages.success(request,
                             ("Your comment is awaiting approval"))

        # if opinion form not valid return empty form
        else:
            opinion_form = OpinionForm()

        # combine template with context dict for article with liked opinions
        return render(
            request,
            "biketalk/article_content.html",
            {
                "article": article,
                "opinions": opinions,
                "opinioned": True,
                "opinion_form": opinion_form,
                "liked": liked
            },
        )


class ArticleLike(View):
    """ article like feature """
    # post request
    def post(self, request, slug):
        """ get the relevant post """
        article = get_object_or_404(Article, slug=slug)
        # filter on user id
        if article.likes.filter(id=request.user.id).exists():
            # if exists, then been liked, so remove it
            article.likes.remove(request.user)
        else:
            # if not already liked, then need to add like
            article.likes.add(request.user)

        # slug determines which post to load
        # when post is liked/unliked, page will reload
        return HttpResponseRedirect(reverse('article_content', args=[slug]))
