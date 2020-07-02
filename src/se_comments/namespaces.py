import enum

from . import core


class Core(core.Namespace, enum.Flag):
    NONE = 0

    @core.flag_field(1 << 0, names=("@", "At"))
    def AT(self, values):
        if not values:
            raise core.CommentError("There is no point in using Core.@ without a name.")
        else:
            return f"@{values[0][0]}".replace(" ", "")

    @core.flag_field(1 << 1, names=("H", "Hi"))
    def HI(self, values):
        if not values:
            raise core.CommentError(
                "There is no point in using Core.Hi without a name."
            )
        else:
            return f"Hi {values[0][0]}."

    @core.flag_field(1 << 2, names=("W", "Welcome"))
    def WELCOME(self, values):
        if not values:
            return "Welcome to Code Review."
        else:
            return f"Welcome to Code Review {values[0][0]}."

    @core.flag_field(1 << 3, names=("VTC", "Vote To Close", "C", "Close"))
    def CLOSE(self, values):
        start = "Unfortunately your question is currently "
        middle = "[off-topic](/help/on-topic)."
        end = " Once you have fixed the issues with your post we'll be happy to review your code."
        if values:
            middle = "off-topic. " + " ".join(CodeReviewCloseReasons.formap(values))
        return start + middle + end

    @core.flag_field(1 << 4, names=("SP", "Site Policy"))
    def SITE_POLICY(self, values):
        return " ".join(CodeReviewSitePolicy.formap(values))

    @core.flag_field(1 << 5, names=("SO", "Stack Overflow"))
    def SO(self, values):
        return " ".join(StackOverflowComments.formap(values))


class CodeReviewCloseReasons(core.Namespace, enum.Flag):
    NONE = 0

    @core.flag_field(1 << 0, names=("Broken", "CNWAI", "Code Not Working As Intended"))
    def BROKEN(self, values):
        end = ""
        if values:
            message = core.english_join(
                CodeReviewBroken.formap(values), sep="; ", oxford=True
            )
            end = f" Since {message} we can see the code is not working correctly."
        return (
            "We only review [code that works as intended](//codereview.meta.stackexchange.com/a/3650)."
            + end
        )

    @core.flag_field(1 << 1, names=("Context", "MRC", "Missing Review Context"))
    def CONTEXT(self, values):
        return "The code you have posted is [missing context](//codereview.meta.stackexchange.com/a/3652) to be reasonably reviewed."

    @core.flag_field(1 << 2, names=("CNI", "Code Not Implemented"))
    def IMPLEMENTED(self, values):
        return "You are asking about [code that has not been implemented](//codereview.meta.stackexchange.com/a/3651)."

    @core.flag_field(1 << 3, names=("BP", "Best Practice"))
    def BEST_PRACTICE(self, values):
        return "[Generic best practice questions](//codereview.meta.stackexchange.com/a/3652) cannot be reasonably answered."

    @core.flag_field(1 << 4, names=("AoM", "Author or Maintainer"))
    def AUTHOR(self, values):
        return "We only review code from an [author or maintainer of the code](//codereview.meta.stackexchange.com/questions/1294)."

    @core.flag_field(1 << 5, names=("MD", "Missing Description"))
    def DESCRIPTION(self, values):
        return "Questions must [include a description of what the code does](//codereview.meta.stackexchange.com/q/1226)."

    @core.flag_field(1 << 6, names=("DR", "Design Review"))
    def DESIGN(self, values):
        return "Design questions, like any other question, must include code."

    @core.flag_field(1 << 7, names=("EoC", "Explanation of Code"))
    def EXPLANATION(self, values):
        return "We do not [explain how code works](//codereview.meta.stackexchange.com/a/3654)."

    @core.flag_field(1 << 8, names=("I", "Inline"))
    def INLINE(self, values):
        return "The code to be reviewed must be [inline in the question](//codereview.meta.stackexchange.com/q/1308)."

    @core.flag_field(1 << 9, names=("Golf",))
    def GOLF(self, values):
        return "Golfing is the dark side of the force."


class CodeReviewBroken(core.Namespace, enum.Flag):
    NONE = 0

    @core.flag_field(1 << 0, names=("Q", "Quote"))
    def QUOTE(self, values):
        message = core.english_join([f'"{v[0].strip()}"' for v in values])
        return f"you've said {message}"

    @core.flag_field(1 << 1, names=("T", "Talk", "Talking"))
    def TALK(self, values):
        message = core.english_join([v[0].strip() for v in values])
        return f"you're talking about {message}"

    @core.flag_field(1 << 2, names=("A", "Ask", "Asking"))
    def ASKING(self, values):
        message = core.english_join([v[0].strip() for v in values])
        return f"you're asking us {message}"


class CodeReviewSitePolicy(core.Namespace, enum.Flag):
    NONE = 0

    @core.flag_field(1 << 0, names=("T", "Title"))
    def TITLE(self, values):
        return "[Titles](/help/how-to-ask) should only consist of a description of your code."

    @core.flag_field(1 << 1, names=("IO", "Insightful Observation"))
    def NO_REVIEW(self, values):
        return "Answers must make at least one [insightful observation](/help/how-to-answer), and must explain why the change is better than the OP's code."

    @core.flag_field(1 << 2, names=("AI", "Answer Invalidation"))
    def AI(self, values):
        return "Please do not update the code in your question to incorporate feedback from answers, doing so goes against the Question + Answer style of Code Review. This is not a forum where you should keep the most updated version in your question. Please see *[what you may and may not do after receiving answers](//codereview.meta.stackexchange.com/a/1765)*."

        # incorporating feedback
        # Adding new code
        # Vandalism


class StackOverflowComments(core.Namespace, enum.Flag):
    NONE = 0

    @core.flag_field(1 << 0, names=("FP", "False Positive"))
    def FALSE_POSITIVE(self, values):
        raise core.CommentError("False positives don't generate messages")

    @core.flag_field(1 << 1, names=("C", "Close", "Closed"))
    def CLOSE(self, values):
        return "[Don't use the existence of Code Review as a reason to close a question](//meta.stackoverflow.com/q/287400). Evaluate the question and use a reason like; needs focus, primarily opinion-based, etc."

    @core.flag_field(1 << 2, names=("R", "Recommendation"))
    def RECOMMENDATION(self, values):
        if not values:
            return f"This question would be off-topic on Code Review."
        reasons = core.english_join(StackOverflowCloseReasons.formap(values))
        return f"This question would be off-topic on Code Review as it {reasons}."

    @core.flag_field(1 << 3, names=("W", "Wording"))
    def WORDING(self, values):
        message = core.english_join(StackOverflowWording.formap(values))
        return f'In the future please {message} when recommending Code Review. Take, "This may be on-topic on Code Review. Please check [if it is on-topic](//codereview.stackexchange.com/help/on-topic) and [how to post a good question](//codereview.stackexchange.com/help/how-to-ask) before posting there."'

    @core.flag_field(1 << 4, names=("I", "Insight"))
    def INSIGHT(self, values):
        return "Please familiarize yourself with what is [on-topic](//codereview.stackexchange.com/help/on-topic) and our [guide to Code Review for Stack Overflow users](//codereview.meta.stackexchange.com/a/5778)."

    def validate(self):
        value = self.NONE
        if self & self.RECOMMENDATION:
            value |= self.RECOMMENDATION
            if not self & self.WORDING:
                value |= self.INSIGHT
        if self & self.CLOSE:
            if self & self.WORDING:
                raise core.CommentError("Cannot mix W and C")
            value |= self.CLOSE
        if self & self.WORDING:
            value |= self.WORDING
        if self & self.INSIGHT:
            raise core.CommentError("Cannot use I")
        if self & self.FALSE_POSITIVE:
            if value != self.NONE:
                raise core.CommentError("Cannot mix FP with other flags")
            value |= self.FALSE_POSITIVE
        return value


class StackOverflowWording(core.Namespace, enum.Flag):
    NONE = 0

    @core.flag_field(1 << 0, names=("D", "Doubtful"))
    def DOUBTFUL(self, values):
        return "use doubtful wording"

    @core.flag_field(1 << 1, names=("L", "Link"))
    def LINK(self, values):
        return "link to the help center"

    def validate(self):
        if self == self.NONE:
            self = self.DOUBTFUL | self.LINK
        return self


class StackOverflowCloseReasons(core.Namespace, enum.Flag):
    NONE = 0

    @core.flag_field(1 << 0, names=("Broken", "CNWAI", "Code Not Working As Intended"))
    def BROKEN(self, values):
        return "does not work as intended"

    @core.flag_field(1 << 1, names=("Context", "MRC", "Missing Review Context"))
    def CONTEXT(self, values):
        return "is missing context"

    @core.flag_field(1 << 2, names=("CNI", "Code Not Implemented"))
    def IMPLEMENTED(self, values):
        return "is asking us to implement code"

    @core.flag_field(1 << 3, names=("BP", "Best Practice"))
    def BEST_PRACTICE(self, values):
        return "is asking about generic best practices"

    @core.flag_field(1 << 4, names=("AoM", "Author or Maintainer"))
    def AUTHOR(self, values):
        return "is not the OP's code"

    @core.flag_field(1 << 5, names=("MD", "Missing Description"))
    def DESCRIPTION(self, values):
        return "is lacking an explanation of the code"

    @core.flag_field(1 << 6, names=("DR", "Design Review"))
    def DESIGN(self, values):
        return "is asking for a review of design not code"

    @core.flag_field(1 << 7, names=("EoC", "Explanation of Code"))
    def EXPLANATION(self, values):
        return "is asking us to explain the code"

    @core.flag_field(1 << 8, names=("I", "Inline"))
    def INLINE(self, values):
        return "does not have the code in the question"

    @core.flag_field(1 << 9, names=("Golf",))
    def GOLF(self, values):
        return "is asking about golfing"
