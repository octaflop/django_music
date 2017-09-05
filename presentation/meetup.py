
# coding: utf-8

# # Intro to Web Development with Django
# # Faris Chebib

# ### A basic web page `web_page`

# Once django is set up, we can use a simple view to render a template

# In[5]:


from django.shortcuts import render

def web_page(request):
    template_name = 'web_page/base.html'
    render(request, template_name, {})


# ### A basic web app `web_app`
