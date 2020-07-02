Comment Micro-language
======================

Rational
--------

What's the point in `yet another auto comments <https://codereview.meta.stackexchange.com/q/4952>`_?

1.  I frequently forget to install the auto comments script, leaving me without any auto comments.
2.  There is no way to merge comments with the auto comments script.
    This means that we either need to write greetings anyway or have two or more versions of each script for greetings alone.
    This means greetings will just be dropped as typing goes against the point of having auto comments.

    Now if we take into account that there can be multiple problems with a single question, then making a mixture of auto comments becomes unmaintainable.
3.  Personally I find some of the current auto comments to be very specific.
    Whilst this is great when we have to deal with that one solution, it makes the auto comments somewhat nonsensical in other situations.

    Say we had an auto comment that had a greeting prepend to it, would it make sense to use that with a 10k user?
    Would you edit it out?

All of these made me drop auto comments for long periods of time.
And I feel I'm posting more helpful content because it's keeping things to the problem(s) at hand.
Not hiding any and not adding unneeded information.

However this has a couple of major problems.

-   I am lazy. Whilst I know there's a page that will really help the user and I should add it to my comment, I don't.
    This means at times I am outputting unhelpful comments.
-   I make mistakes. Sometimes I miss a crucial part of a comment. Contrast "please don't post many similar questions" vs "please don't post many similar questions in short time periods".
    This can cause there to be confusion and is again unhelpful.

Whilst this is good for me there are some problems with my approach.

-   You may not have Python installed, or have the Python-foo to install this project.
-   You may not like a CLI only program, I have to open a terminal? No thanks.
-   You may not like my comment choices, and you don't know how to change them.
-   You want simple auto comments, you don't want to have to type short hand for your comments.
-   You don't know the short hand or names I have used.

Syntax
------

The syntax is really basic, and looks a lot like a list literal from Python or JavaScript.
However the outermost 'list' doesn't have the square brackets.
However it does not build lists it builds a dictionary, the keys are on the left hand side of the brackets and the keys of the child mapping are on the inside of the brackets.
All keys surrounding whitespace stripped.

..  code:: none

    Welcome[John Doe],
    VTC[
        Broken[
            Quote[this does not work],
            Asking[to fix this],
        ],
        Inline,
    ],
    Scope[Title]

Contrast to if we were to use JSON:

..  code:: json

    {
        "Welcome": {"John Doe": {}},
        "VTC": {
            "Broken": {
                "Quote": {"this does not work": {}},
                "Asking": {"to fix this": {}}
            },
            "Inline": {}
        },
        "Scope": {"Title": {}}
    }

There are only 4 characters that are recognized:

1.  Opening brackets, ``[``. These denote the start of a mapping.
2.  Closing brackets, ``]``. These denote the end of a mapping.
3.  A comma, ``,``. These are used to split two keys where the first doesn't have any values.
4.  A backslash, ``\``. This is to escape the next character.

It should be noted that this means that commas are entirely optional following closing brackets.

Namespaces
----------

From here the keys map to keys in a namespace. For example ``Welcome`` means points to the global ``Welcome`` which will take the entered name and return the welcome greeting.
The ``VTC`` however causes the inner dictionary to be passed to the VTC namespace.

Each namespace accepts multiple keys for the same function.
This means you can use the long form ``Welcome[John Doe]`` or the short form ``W[John Doe]``.
The keys on namespaces are also case insensitive and ignore spaces, this means ``Vote to Close`` is the same as ``votetoclose``.

This is a key to make skim reading easier:

🔗
    Contains a link to a relevant page.

📜
    Changes the output of the text.

📚
    Indicates that it points to a namespace.

🚩
    Produce an error

Global
++++++

The global namespace contains:

``@`` ``At``
    Will strip spaces in the name.

    🚩 Empty
        There is no point in using Core.@ without a name.
    📜 Else
        @{value}

``H`` ``Hi``
    🚩 Empty
        There is no point in using Core.Hi without a name.
    📜 Else
        Hi {value}.

📜 ``W`` ``Welcome``
    Empty
        Welcome to Code Review.
    Else
        Welcome to Code Review {value}.

📜 ``VTC`` ``Vote To Close`` ``C`` ``Close``
    🔗 Empty
        Unfortunately your question is currently `off-topic <https://codereview.stackexchange.com/help/on-topic>`_. Once you have fixed the issues with your post we'll be happy to review your code.
    📚 Else
        Enter `close reasons namespace <#close-reasons>`_.
    
        Unfortunately your question is currently off-topic. {messages} Once you have fixed the issues with your post we'll be happy to review your code.

📚 ``SP`` ``Site Policy``
    Enter `site policy namespace <#site-policy>`_.


📚 ``SO`` ``Stack Overflow``
    Enter `Stack Overflow namespace <#stack-overflow>`_.

Close Reasons
+++++++++++++

🔗 📜 ``Broken`` ``CNWAI`` ``Code Not Working As Intended``
    We only review `code that works as intended <https://codereview.meta.stackexchange.com/a/3650>`_.

    📜 📚 Not Empty
        Since {messages} we can see the code is not working correctly.

        📜 ``Q`` ``Quote``
            you've said {values}
        
        📜 ``T`` ``Talk`` ``Talking``
            you're talking about {values}
        
        📜 ``A`` ``Ask`` ``Asking``
            you're asking us {values}

🔗 📜 ``Context`` ``MRC`` ``Missing Review Context``
    The code you have posted is `missing context <https://codereview.meta.stackexchange.com/a/3652>`_ to be reasonably reviewed.

🔗 📜 ``CNI`` ``Code Not Implemented``
    You are asking about `code that has not been implemented <https://codereview.meta.stackexchange.com/a/3651>`_.

🔗 📜 ``BP`` ``Best Practice``
    `Generic best practice questions <https://codereview.meta.stackexchange.com/a/3652>`_ cannot be reasonably answered.

🔗 📜 ``AoM`` ``Author or Maintainer``
    We only review code from an `author or maintainer of the code <https://codereview.meta.stackexchange.com/questions/1294>`_.

🔗 📜 ``MD`` ``Missing Description``
    Questions must `include a description of what the code does <https://codereview.meta.stackexchange.com/q/1226>`_.

📜 ``DR`` ``Design Review``
    Design questions, like any other question, must include code.

🔗 📜 ``EoC`` ``Explanation of Code``
    We do not `explain how code works <https://codereview.meta.stackexchange.com/a/3654>`_.

🔗 📜 ``I`` ``Inline``
    The code to be reviewed must be `inline in the question <https://codereview.meta.stackexchange.com/q/1308>`_.

📜 ``Golf``
    Golfing is the dark side of the force.

Site Policy
+++++++++++

🔗 📜 ``T`` ``Title``
    `Titles <https://codereview.stackexchange.com/help/how-to-ask>`_ should only consist of a description of your code.

🔗 📜 ``IO`` ``Insightful Observation``
    Answers must make at least one `insightful observation <https://codereview.stackexchange.com/help/how-to-answer>`_, and must explain why the change is better than the OP's code.

🔗 📜 ``AI`` ``Answer Invalidation``
    Please do not update the code in your question to incorporate feedback from answers, doing so goes against the Question + Answer style of Code Review. This is not a forum where you should keep the most updated version in your question. Please see `what you may and may not do after receiving answers <https://codereview.meta.stackexchange.com/a/1765>`_.

Stack Overflow
++++++++++++++

🚩 ``FP`` ``False Positive``
    False positives don't generate messages

🔗 📜 ``C`` ``Close`` ``Closed``
    `Don't use the existence of Code Review as a reason to close a question <https://meta.stackoverflow.com/q/287400>`_. Evaluate the question and use a reason like; needs focus, primarily opinion-based, etc.

📜 ``R`` ``Recommendation``
    Empty
        This question would be off-topic on Code Review.
    📚 Else
        Enter `Stack Overflow close votes namespace <#stack-overflow-close-reasons>`_.

        This question would be off-topic on Code Review as it {messages}.

🔗 📜 📚 ``W`` ``Wording``
    In the future please {messages} when recommending Code Review. Take, "This may be on-topic on Code Review. Please check `if it is on-topic <https://codereview.stackexchange.com/help/on-topic>`_ and `how to post a good question <https://codereview.stackexchange.com/help/how-to-ask>`_ before posting there."

    📜 ``D`` ``Doubtful``
        use doubtful wording

    📜 ``L`` ``Link``
        link to the help center

🔗 📜 ``I`` ``Insight``
    Please familiarize yourself with what is `on-topic <https://codereview.stackexchange.com/help/on-topic>`_ and our `guide to Code Review for Stack Overflow users <https://codereview.meta.stackexchange.com/a/5778>`_.

Stack Overflow Close Reasons
++++++++++++++++++++++++++++

📜 ``Broken`` ``CNWAI`` ``Code Not Working As Intended``
    does not work as intended

📜 ``Context`` ``MRC`` ``Missing Review Context``
    is missing context

📜 ``CNI`` ``Code Not Implemented``
    is asking us to implement code

📜 ``BP`` ``Best Practice``
    is asking about generic best practices

📜 ``AoM`` ``Author or Maintainer``
    is not the OP's code

📜 ``MD`` ``Missing Description``
    is lacking an explanation of the code

📜 ``DR`` ``Design Review``
    is asking for a review of design not code

📜 ``EoC`` ``Explanation of Code``
    is asking us to explain the code

📜 ``I`` ``Inline``
    does not have the code in the question

📜 ``Golf``
    is asking about golfing
