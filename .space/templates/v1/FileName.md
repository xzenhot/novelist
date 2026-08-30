  public enum OperationState
  {
      // Initial state, no operation performed yet.
      None = 0,
      // If any error happens during the execution of an activity, the error message will be stored in this state. This can be used by model to decide how to fix the error and continue the execution.
      Exception = 4,
      //Not used so far
      InputModelJson = 10,
      //Initial model, which may be modified
      SelfStateInitialJson = 11,
      //StrongType - State checksum
      SelfStateActivityJson = 12,

      TemplateSystemPromptText = 20,
      // These dictionary comes from initialize section, never updated. Used to pass parameters to template.
      TemplateModelJson = 22,
      // Example Schema for template layout, which may be used by model to understand how to fill the content.
      TemplateLayOutShapeJson = 23,
      // Initial template prompt text created by template, first item of an array of prompt text, which may be modified by model.
      TemplatePromptInitialText = 24,
      // Next template prompt text created by template, which may be modified by model.
      TemplatePromptNextText = 25,
      // Summary template prompt text created by template, which may be modified by model.
      TemplatePromptSummaryText = 26,
      TemplatePromptTranslateText = 27,

      // While executing agent, this is the actual prompt text sent to model, which may be modified by model before sending to next agent.
      ActualPromptAgentText = 30,
      // While executing agent, this is the actual prompt text sent to model with human in the loop, which may be modified by model before sending to next agent.
      HumanInTheLoopPromptText = 31,

      // Actual parameters used to create actual prompt, which may be modified by model before sending to next agent.
      ModelDictionaryJson = 32,

      // Raw response text received from model, which may be modified by model before sending to next agent.
      ReceivedAgentResponseText = 50,
      // Parsed response in json format received from model, which may be modified by model before sending to next agent.
      ExtractedAgentResponseJson = 60,

      // Calculated summary text based on model response and content, which may be modified by model before sending to next agent.
      RunningContentSummaryText = 82,
      TranslatedContentText = 83,
      ReviwedContentText = 84,
      // Last object returned from an method of an activity method of a workflow. This is the final output of an activity. This can not be modified.
      ReturningModelJson = 90,

      // Final content text after an activity. This is the final output of an activity. This can not be modified.
      FinalContentText = 100,
      TemplatePromptSingleSegmentText = 101
  }