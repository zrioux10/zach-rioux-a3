import { lazy, Suspense, useMemo, useState } from "react";
import ReactMarkdown from "react-markdown";
import * as core from "@mantine/core";

import { TrialsComponent } from "../parser/types";
import TextInput from "../components/stimuli/inputcomponents/TextInput";

import { useDispatch } from "react-redux";
import { saveAnswer } from '../store/'

export default function Trials({
  goToNextSection,
  currentStudySectionConfig,
}: {
  goToNextSection: () => void;
  currentStudySectionConfig: TrialsComponent;
}) {
  const dispatch = useDispatch();
  const [stimuliIndex, setStimuliIndex] = useState(0);

  const stimuliSequence = useMemo(() => {
    return currentStudySectionConfig.order;
  }, [currentStudySectionConfig]);

  // current active stimuli presented to the user
  const stimulusID = stimuliSequence[stimuliIndex];
  const stimulus = currentStudySectionConfig.trials[stimulusID];

  const [answer, setAnswer] = useState("");
  const goToNext = () => {
    dispatch(saveAnswer({ [stimulusID]: answer }));

    if (isLastStimulus) {
      goToNextSection()
    } else {
      setStimuliIndex(stimuliIndex + 1);
    }
  };

  const isLastStimulus = stimuliIndex === stimuliSequence.length - 1;

  const StimulusComponent = lazy(() => import(/* @vite-ignore */`../components/${stimulus.stimulus.path}`));

  return (
    <div>
      <ReactMarkdown>{stimulus.instruction}</ReactMarkdown>
      <Suspense fallback={<div>Loading...</div>}>
        <StimulusComponent />
        <TextInput placeholder={"The answer is range from 0 - 100"} label={"Your answer"} updateAnswerInParent={setAnswer} />
      </Suspense>
      
      <core.Group position="right" spacing="xs" mt="xl">
        <core.Button onClick={goToNext}>Next</core.Button>
      </core.Group>
    </div>
  );
}
