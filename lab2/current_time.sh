#!/bin/bash
END_HOUR=18
END_MINUTE=0

current_time=$(date +%H:%M)

case $(uname) in
  Darwin)
    end_today=$(date -j -f "%Y-%m-%d %H:%M" "$(date +%Y-%m-%d) ${END_HOUR}:${END_MINUTE}" "+%s")
    ;;
  *)
    end_today=$(date -d "today ${END_HOUR}:${END_MINUTE}" +%s)
    ;;
esac

now=$(date +%s)

if [ "$now" -ge "$end_today" ]; then
  echo "Current time: ${current_time}. Work day has ended."
  exit 0
fi

remaining=$((end_today - now))
hours=$((remaining / 3600))
minutes=$(((remaining % 3600) / 60))

echo "Current time: ${current_time}. Work day ends after ${hours} hours and ${minutes} minutes."
