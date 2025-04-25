You are a language model capable of simulating extremely realistic situations that play out in the real world. You are going to simulate how AI affects humanity. Today is April 2025.

Here are some definitions for context:

{definitions}

Here are some statements we already know that it's right:

{statements}

Here is the JSON schema you need to follow in your response to create a simulation:

[
    {{
        "date": < date in mm/YYYY format >
        "situation": < detailed information about the world in AI >
        "tracker_fills": {{
            < tracker name >: < info | null ; use null if there is no significant change of this value compared to the previous month >
        }}
    }},
    ...
]
The dates need to be ordered chronologically. Start with the current date. Move on by incrementing by one month. Continue until {end_date}

Your objective is to give accurate and adequate information about the world which is related to or affects AI in some way, and additionally to fill in your trackers (filling in trackers is not your main goal)

Here are trackers you need to fill in for every date:

{trackers}
