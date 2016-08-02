# -*- coding: utf-8 -*-
#
# AWS Sphinx configuration file.
#
# For more information about how to configure this file, see:
#
# https://w.amazon.com/index.php/AWSDevDocs/Sphinx
#

#
# General information about the project.
#

# Optional service/SDK name, typically the three letter acronym (TLA) that
# represents the service, such as 'SWF'. If this is an SDK, you can use 'SDK'
# here.
service_name = "TKV"

# The long version of the service or SDK name, such as "Amazon Simple Workflow
# Service", "AWS Flow Framework for Ruby" or "AWS SDK for Java"
service_name_long = u'AWS Toolkit for Visual Studio'

# The landing page for the service documentation.
service_docs_home = u'http://aws.amazon.com/documentation/visualstudio/'

# The project type, such as "Developer Guide", "API Reference", "User Guide",
# or whatever.
project = u'User Guide'

# A short description of the project.
project_desc = ' '.join([service_name_long, project])

# the output will be generated in latest/<project_basename> and
# its URL will feature the same basename.
project_basename = 'UserGuide'

# This name is used as the manual / PDF name. Don't include the extension
# (.pdf) here.
man_name = 'aws-tkv-ug'

# The language for this version of the docs. Typically 'en'. For a full list of
# values, see: http://sphinx-doc.org/config.html#confval-language
language = u'en'

# Whether or not to show the PDF link. If you generate a PDF for your
# documentation, set this to True.
show_pdf_link = True

#
# Version Information
#

# The version info for the project you're documenting, used as values for the
# |version| and |release| substitutions.
#
# The short X.Y version.

version = '1.0'

# The full version, including alpha/beta/rc tags.

release = '1.0'


#
# Forum Information
#

# Optional forum ID. If there's a relevant forum at forums.aws.amazon.com, then
# set the ID here. If not set, then no forum ID link will be generated.
#

forum_id = '61'


#
# Extra Navlinks
#

# Extra navlinks. You can specify additional links to appear in the top bar here
# as navlink name / url pairs. If extra_navlinks is not set, then no extra
# navlinks will be generated.
#
# extra_navlinks = [
#         ('API Reference', 'http://path/to/api/reference'),
#         ('GitHub', 'http://path/to/github/project'),
#         ]

extra_navlinks = []

#
# EXTRA_CONF_CONTENT -- don't change, move or remove this line!
#
# Any settings *below* this act as overrides for the default config content.
# Declare extlinks <http://sphinx-doc.org/latest/ext/extlinks.html> and
# additional configuration details specific to this documentation set here.
#
# usage: :mktplace-search:`Amazon Machine Images <AMISAWS>` where AMISAWS is the search term.
# usage: :mktplace-search:`Windows server <windows+server>` 
aws_docs_url = 'http://docs.aws.amazon.com/'
aws_url = 'https://aws.amazon.com/'
aws_blogs = 'http://blogs.aws.amazon.com/'
aws_blogs_net = aws_blogs + 'net/post/'

if 'extlinks' not in vars():
    extlinks = {}

#unsubmitted
extlinks['eb-dg-deep']  = (aws_docs_url + 'elasticbeanstalk/latest/dg/%s', '')
extlinks['ddb-dg-deep']  = (aws_docs_url + 'dynamodb/latest/dg/%s', '')
extlinks['mktplace-search'] = (aws_url + 'marketplace/search/results/&searchTerms=%s?browse=1', '')
extlinks['ec2-faq']         = (aws_url + 'ec2/faqs/%s', '')
extlinks['s3-faq']          = (aws_url + 's3/faqs/%s', '')
extlinks['aws-articles']    = (aws_url + 'articles/%s', '')

# http://blogs.aws.amazon.com/net/post/Tx1P7UD2UN3DHK6/Overriding-Endpoints-in-the-AWS-SDK-for-NET
# pass in everything after post/
extlinks['aws-blogs-net'] = (aws_blogs_net + '%s', '')
extlinks['aws-blogs']     = (aws_blogs + '%s', '')
