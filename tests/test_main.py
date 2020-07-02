from pytest import raises
from se_comments import CommentError, __main__, main

TESTS = [
    (
        "Stack Overflow[Wording]",
        'In the future please use doubtful wording and link to the help center when recommending Code Review. Take, "This may be on-topic on Code Review. Please check [if it is on-topic](//codereview.stackexchange.com/help/on-topic) and [how to post a good question](//codereview.stackexchange.com/help/how-to-ask) before posting there."',
    ),
    (
        "SO[Close]",
        "[Don't use the existence of Code Review as a reason to close a question](//meta.stackoverflow.com/q/287400). Evaluate the question and use a reason like; needs focus, primarily opinion-based, etc.",
    ),
    (
        "SO[Recommendation,Wording]",
        'This question would be off-topic on Code Review. In the future please use doubtful wording and link to the help center when recommending Code Review. Take, "This may be on-topic on Code Review. Please check [if it is on-topic](//codereview.stackexchange.com/help/on-topic) and [how to post a good question](//codereview.stackexchange.com/help/how-to-ask) before posting there."',
    ),
    (
        "SO[R[Code Not Working As Intended, Missing Review Context, Code Not Implemented, Best Practice, Author or Maintainer, Missing Description, Design Review, Explanation of Code, Inline, Golf]]",
        "This question would be off-topic on Code Review as it does not work as intended, is missing context, is asking us to implement code, is asking about generic best practices, is not the OP's code, is lacking an explanation of the code, is asking for a review of design not code, is asking us to explain the code, does not have the code in the question and is asking about golfing. Please familiarize yourself with what is [on-topic](//codereview.stackexchange.com/help/on-topic) and our [guide to Code Review for Stack Overflow users](//codereview.meta.stackexchange.com/a/5778).",
    ),
    (
        "Hi[John Doe], Site Policy[Title]",
        "Hi John Doe. [Titles](/help/how-to-ask) should only consist of a description of your code.",
    ),
    ("Welcome", "Welcome to Code Review.",),
    (
        "W[John Doe], SP[Insightful Observation]",
        "Welcome to Code Review John Doe. Answers must make at least one [insightful observation](/help/how-to-answer), and must explain why the change is better than the OP's code.",
    ),
    (
        "@[John Doe],SP[Answer Invalidation]",
        "@JohnDoe Please do not update the code in your question to incorporate feedback from answers, doing so goes against the Question + Answer style of Code Review. This is not a forum where you should keep the most updated version in your question. Please see *[what you may and may not do after receiving answers](//codereview.meta.stackexchange.com/a/1765)*.",
    ),
    (
        "Vote To Close",
        "Unfortunately your question is currently [off-topic](/help/on-topic). Once you have fixed the issues with your post we'll be happy to review your code.",
    ),
    (
        "VTC[broken[Quote[I have an issue\\, it boops], Talk[a bug, an error, incorrect output], Ask[to fix something]]]",
        "Unfortunately your question is currently off-topic. We only review [code that works as intended](//codereview.meta.stackexchange.com/a/3650). Since you've said \"I have an issue, it boops\"; you're talking about a bug, an error and incorrect output; and you're asking us to fix something we can see the code is not working correctly. Once you have fixed the issues with your post we'll be happy to review your code.",
    ),
    (
        "VTC[Broken,MRC,CNI,BP,AoM,MD,DR,EoC,I,Golf]",
        "Unfortunately your question is currently off-topic. We only review [code that works as intended](//codereview.meta.stackexchange.com/a/3650). The code you have posted is [missing context](//codereview.meta.stackexchange.com/a/3652) to be reasonably reviewed. You are asking about [code that has not been implemented](//codereview.meta.stackexchange.com/a/3651). [Generic best practice questions](//codereview.meta.stackexchange.com/a/3652) cannot be reasonably answered. We only review code from an [author or maintainer of the code](//codereview.meta.stackexchange.com/questions/1294). Questions must [include a description of what the code does](//codereview.meta.stackexchange.com/q/1226). Design questions, like any other question, must include code. We do not [explain how code works](//codereview.meta.stackexchange.com/a/3654). The code to be reviewed must be [inline in the question](//codereview.meta.stackexchange.com/q/1308). Golfing is the dark side of the force. Once you have fixed the issues with your post we'll be happy to review your code.",
    ),
]
TEST_ERRORS = [
    ("KEY_ERROR", "Unknown input 'KEY_ERROR'",),
    ("@", "There is no point in using Core.@ without a name.",),
    ("H", "There is no point in using Core.Hi without a name.",),
    ("SO[False Positive]", "False positives don't generate messages",),
    ("SO[W, C]", "Cannot mix W and C",),
    ("SO[Insight]", "Cannot use I",),
    ("SO[R, FP]", "Cannot mix FP with other flags",),
]


def test_core():
    for input, output in TESTS:
        assert main(input) == output


def test_unknown_key():
    for input, message in TEST_ERRORS:
        with raises(CommentError, match=message):
            main(input) == output
